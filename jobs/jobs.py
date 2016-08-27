import discord
import os
import asyncio
import datetime
from cogs.utils.dataIO import dataIO
from discord.ext import commands
from __main__ import send_cmd_help
from .economy import NoAccount, NegativeValue

class Jobs:
    """Jobs"""

    def __init__(self, bot):
        self.bot = bot
        self.jobs = dataIO.load_json("data/jobs/jobs.json")
        self.active_jobs = []

    @commands.group(pass_context=True)
    async def work(self, ctx):
        """Work commands"""
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

    @work.command(pass_context=True)
    async def start(self, ctx, *, job : str):
        """Starts working"""
        server = ctx.message.server
        jobs = self.jobs.get(server.id, [])
        author = ctx.message.author
        has_account = self.check_account(author)
        if has_account is False:
            await self.bot.say("You need a bank account first. {}bank register".format(ctx.prefix))
            return
        elif has_account is None:
            await self.bot.say("Economy cog doesn't seem to be loaded. Contact the owner.")
            return
        if not self.is_user_working(author):
            if job in jobs:
                if self.is_user_eligible(author, job, jobs):
                    new_job = ActiveJob(message=ctx.message, job_name=job, cog=self)
                    self.active_jobs.append(new_job)
                    #print(self.active_jobs)
                    await self.bot.say("You started working.")
                else:
                    await self.bot.say("You don't have the appropriate role for this job.")
            else:
                await self.bot.say("There's no such job.")
        else:
            await self.bot.say("You're already working.")

    @work.command(pass_context=True)
    async def stop(self, ctx):
        """Stops working"""
        author = ctx.message.author
        for job in self.active_jobs:
            if job.member == author:
                self.active_jobs.remove(job)
                #print(self.active_jobs)
                await self.bot.say("You stopped working.")
                return
        else:
            await self.bot.say("You're not working any job")

    @commands.group(pass_context=True)
    async def job(self, ctx):
        """Jobs related commands"""
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

    @job.command(pass_context=True)
    async def add(self, ctx, job : str, time : int, payout : int, role : discord.Role=None):
        """Adds job"""
        server = ctx.message.server
        job = job.lower()
        self.jobs.setdefault(server.id, {})
        jobs = self.jobs[server.id]
        role = role.name if role is not None else None
        if job not in jobs:
            jobs[job] = {
                "time" : time,
                "payout" : payout,
                "role" : role
                }
            await self.bot.say("Job added.")
            dataIO.save_json("data/jobs/jobs.json", self.jobs)
        else:
            await self.bot.say("A job with that name already exists.")

    @job.command(pass_context=True)
    async def remove(self, ctx, *, job : str):
        """Removes job"""
        server = ctx.message.server
        job = job.lower()
        jobs = self.jobs.get(server.id, {})
        if job in jobs:
            self.remove_active_jobs_by_name(job)
            del jobs[job]
            await self.bot.say("Job deleted.")
            dataIO.save_json("data/jobs/jobs.json", self.jobs)
        else:
            await self.bot.say("That job doesn't exist.")

    @job.command(name="list", pass_context=True)
    async def _list(self, ctx):
        """Lists server's jobs"""
        server = ctx.message.server
        jobs = self.jobs.get(server.id, {})
        #print(jobs)
        if jobs:
            msg = "Jobs in this server:\n\n```erlang\n"
            for job in jobs:
                job_name = job
                job = jobs[job]
                msg += "Job: " + job_name + "\n"
                msg += "Payout: {} every {} seconds\n".format(job["payout"], job["time"])
                role_required = "None" if job["role"] is None else job["role"]
                msg += "Role Required: " + role_required + "\n\n"
            msg += "```"
            await self.bot.say(msg)
        else:
            await self.bot.say("There are no jobs in this server.")

    def is_user_working(self, user):
        for job in self.active_jobs:
            if job.member == user:
                return True
        return False

    def remove_active_jobs_by_name(self, job):
        to_remove = []
        for job in self.active_jobs:
            if job.job_name == job:
                to_remove.append(job)
        for job in to_remove:
            self.active_jobs.remove(job)

    def remove_active_jobs_by_member(self, member):
        to_remove = []
        for job in self.active_jobs:
            if job.member == member:
                to_remove.append(job)
        for job in to_remove:
            #print("Removing a job due to offline status")
            self.active_jobs.remove(job)

    def is_user_eligible(self, user, job_name, jobs):
        job = jobs.get(job_name)
        if job["role"] is not None:
            role = discord.utils.get(user.roles, name=job["role"])
            if role is not None:
                return True
            else:
                return False
        else:
            return True

    def check_account(self, user):
        try:
            bank = self.bot.get_cog("Economy").bank
        except AttributeError:
            return None
        if bank.account_exists(user):
            return True
        else:
            return False

    async def on_member_update(self, before, after):
        if after.status.name == "offline":
            self.remove_active_jobs_by_member(after)

    async def check_active_jobs(self):
        while self is self.bot.get_cog("Jobs"):
            for job in self.active_jobs:
                job.check_time()
            await asyncio.sleep(1)

class ActiveJob:
    def __init__(self, *, message, job_name, cog):
        self.member = message.author
        self.server = message.server
        self.job_name = job_name
        self.started = datetime.datetime.now()
        self.cog = cog # Reference to main cog

    def check_time(self):
        server_jobs = self.cog.jobs.get(self.server.id, {})
        job = server_jobs.get(self.job_name, None)
        now = datetime.datetime.now()
        if job:
            if (now - self.started).seconds >= job["time"]:
                self.payout(job)
                self.started = datetime.datetime.now()
                #print("payout time")
        else: # Job no longer exists. This should never happen, as active jobs are supposed to be cleaned on removal
            pass

    def payout(self, job):
        try:
            bank = self.cog.bot.get_cog("Economy").bank
        except AttributeError:
            print("Your economy cog seem to be unloaded. Jobs cog failed to deliver payout.")
            return
        print("Paying {} to {}".format(self.member, job["payout"]))
        try:
            bank.deposit_credits(self.member, job["payout"])
        except NoAccount:
            print("User {} lacks an account. Jobs cog failed to deliver payout".format(self.member))
        except NegativeValue:
            print("Can't deliver to {} a negative payout. Jobs cog failed to deliver payout".format(self.member))


def check_folders():
    if not os.path.exists("data/jobs"):
        print("Creating data/jobs folder...")
        os.makedirs("data/jobs")

def check_files():
    if not dataIO.is_valid_json("data/jobs/jobs.json"):
        print("Creating jobs' jobs.json...")
        dataIO.save_json("data/jobs/jobs.json", {})

def setup(bot):
    check_folders()
    check_files()
    n = Jobs(bot)
    bot.loop.create_task(n.check_active_jobs())
    bot.add_cog(n)
