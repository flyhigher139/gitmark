from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.views.generic import View
from django.shortcuts import render, redirect
# from django.db import IntegrityError
from django.db.models import Count
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import requests

from . import models

PER_PAGE = settings.GITMARK['PER_PAGE']
PER_PAGE_ADMIN = settings.GITMARK['PER_PAGE_ADMIN']

def common_data():
    data = {}
    return data


class EnterpriseView(View):
	template_name = r'main/enterprise.html'
	def get(self, request):
		return render(request, self.template_name)


class AdminIndexView(View):
    template_name = 'myadmin/index.html'
    def get(self, request):
        data = common_data()
        return render(request, self.template_name, data)

class HomeView(View):
    template_name = 'main/home.html'
    def get(self, request):
        data = common_data()
        return render(request, self.template_name, data)

class ImportRepoView(View):
    template_name = 'myadmin/import_repo.html'
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        github_user = request.POST.get('github_username')
        def build_api(user, page):
            return 'https://api.github.com/users/{0}/starred?page={1}'.format(user, page)

        def import_repos(starred_repos):
            for starred_repo in starred_repos:
                language, created = models.Language.objects.get_or_create(name=(starred_repo.get('language') or 'unknown'))

                repo, created = models.Repo.objects.get_or_create(full_name=starred_repo.get('full_name'), 
                    defaults={
                        'name' : starred_repo.get('name'),
                        'link' : starred_repo.get('html_url'),
                        'author' : starred_repo.get('owner').get('login'),
                        'author_link' : starred_repo.get('owner').get('html_url'),
                        'desc' : starred_repo.get('description'),
                        'language' :language
                    })
                # repo_starred, created = models.RepoStarred.objects.get_or_create(repo=repo, user=request.user)
                repo.starred_users.add(request.user)

        # api = 'https://api.github.com/users/{0}/starred?page=1'.format(github_user)
        page = 1
        api = build_api(github_user, page)
        # return redirect(api)
        res = requests.get(api)
        starred_repos = res.json()

        while len(starred_repos) > 0:
            import_repos(starred_repos)

            page += 1
            api = build_api(github_user, page)
            res = requests.get(api)
            starred_repos = res.json()
            

        return HttpResponse('Succeed to import repos')

class StarredRepoView(View):
    template_name = 'myadmin/starred_repo.html'
    def get(self, request):
        data = common_data()
        language_id = request.GET.get('language', 0)
        try:
            language_id = int(language_id)
        except ValueError:
            raise Http404
        data['language_id'] = language_id
        starred_repos = models.Repo.objects.filter(starred_users=request.user)
        languages = starred_repos.values('language').annotate(num_repo=Count('language'))
        for language in languages:
            language['name'] = models.Language.objects.get(pk=language['language']).name
        data['languages'] = languages

        if language_id:        
            starred_repos = starred_repos.filter(language__id=language_id)
            url_parm = '?language={0}'.format(language_id)
            data['url_parm'] = url_parm

        paginator = Paginator(starred_repos, PER_PAGE_ADMIN)
        page = request.GET.get('page')
        try:
            starred_repos = paginator.page(page)
        except PageNotAnInteger:
            starred_repos = paginator.page(1)
        except EmptyPage:
            starred_repos = paginator.page(paginator.num_pages)

        data['starred_repos'] = starred_repos



        return render(request, self.template_name, data)

class MyCollectionView(View):
    template_name = 'myadmin/collections.html'
    def get(self, request):
        data = common_data()
        collections = models.Collection.objects.filter(user=request.user)
        data['collections'] = collections

        return render(request, self.template_name, data)

class MyCollectionDetailView(View):
    template_name = 'myadmin/collection.html'
    def get(self, request, pk):
        pk = int(pk)
        data = common_data()
        collections = models.Collection.objects.filter(user=request.user)
        data['collections'] = collections
        try:
            cur_collection = models.Collection.objects.get(pk=pk)
            data['cur_collection'] = cur_collection
        except models.Collection.ObjectNotExist:
            raise Http404
            
        repos = cur_collection.repos.all()

        paginator = Paginator(repos, PER_PAGE)
        page = request.GET.get('page')
        try:
            repos = paginator.page(page)
        except PageNotAnInteger:
            repos = paginator.page(1)
        except EmptyPage:
            repos = paginator.page(paginator.num_pages)

        # data['starred_repos'] = starred_repos

        data['repos'] = repos

        return render(request, self.template_name, data)



