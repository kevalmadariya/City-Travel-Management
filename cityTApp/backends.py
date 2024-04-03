from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
from .models import Agent

class AgentBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            print("ttttttttttttttttttttt")
            agent = Agent.objects.get(username=username)
            print(agent)
            print(agent.password)
            print(password)
            if password == agent.password:  # Compare passwords using check_password
                return agent
        except Agent.DoesNotExist:
            return None
