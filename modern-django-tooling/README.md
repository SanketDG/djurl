# Modern Django Tooling

This is a series of posts at an _attempt_ to take a very simple Django project
that was written a few years ago, and try to improve the tooling using modern
techniques.

<!-- TOC -->
- [Introduction](#introduction)
- [Use poetry for dependency management (or pip-tools)](#use-poetry-for-dependency-management-or-pip-tools)
- [Easy development environments with Docker and docker-compose](#easy-development-environments-with-docker-and-docker-compose)
- [Integrate static typing with `mypy` and `django-stubs`](#integrate-static-typing-with-mypy-and-django-stubs)
- [Easy linting with `flake8` and `wemake-python-stylguide`](#easy-linting-with-flake8-and-wemake-python-stylguide)
- [Opinionated code formatting using _Black_](#opinionated-code-formatting-using-_black_)
- [Automate typing/linting/formatting on commit using `pre-commit`](#automate-typinglintingformatting-on-commit-using-pre-commit)
- [py.test and GitHub CI integration](#pytest-and-github-ci-integration)
- [Multiple Deployment Options with Herkou and Cloud Run.](#multiple-deployment-options-with-herkou-and-cloud-run)
<!-- /TOC -->

## Introduction

The application in question whose tooling is being attempted to improve,
is just a simple URL shortener called [djurl](../). It does use some of Django's
key features, but nowhere uses and implements some of Django's best features.

I had written this application a few years ago when I had started out with Django,
and now I am using some of my gained knowledge to improve the tooling of this Django
application according to some of the modern standards in Python ecosystem.

----
**Disclaimer**

This is by no means a tutorial on Django or any of its features, nor is it about
implenting Django best practices.

I do not have any accurate metrics on how useful this is for people other than me,
these are some of the personal opinions I have while adopting some of the tooling techniques that has popped up in recent years.

----

## Use poetry for dependency management (or pip-tools)

Packaging and dependency management has always been
[hard in Python](https://blog.ionelmc.ro/2015/02/24/the-problem-with-packaging-in-python/),
in the past, espescially for beginners.

There have been several efforts by the Python community to standardize
dependency management and Poetry is one of many such efforts.

From the [Poetry home page](https://python-poetry.org/)

> - Poetry comes with all the tools you might need to manage your projects in a deterministic way.
> - Easily build and package your projects with a single command.
> - Make your work known by publishing it to PyPI
> - Having an insight of your project's dependencies is just one command away.

Let's get started then!

### Installation

Installation is pretty straight forward from the [docs](https://python-poetry.org/docs/#installation)

----
**Note**

This is an opinionated workflow of how to integrate and use Poetry in your Django projects.

----
### From requirements.txt to pyproject.toml

This is a tricky one! I have searched for tools that would automate this
process, but sadly there is none that works concretely.

The best way to do this is to just bootstrap a new Poetry project from scratch

```shell
$ poetry init --no-interaction --dependency django
```

This will create a new `pyproject.toml` in your project directory. You can pass additional dependencies in the command itself or you can edit the `pyproject.toml`
file after creation:

```
[tool.poetry.dependencies]
python = "^3.6"
Django = "^3.0.6"
dj-database-url = "^0.5.0" # added this
```

[Relevant
commit](https://github.com/SanketDG/djurl/commit/86d29f453a00c702b35f81b1f27207640d563fb6)
where I create a pyproject.toml and run `poetry install` (explained in the next
section)

----
**Note**

[Dephell](https://dephell.readthedocs.io/cmd-deps-convert.html) is a dedicated tool
to convert between known Python packaging formats.

----

### Install dependencies and create virtualenv

Let's install all the poetry dependencies

```shell
$ poetry install
```

Let's take a pause to understand what magic Poetry does here.

Poetry will first install all of the packages listed in `pyproject.toml` in an isolated
virtualenv. It will then lock the exact version of all of the packages that were installed
and write them to `poetry.lock`.

Why do we even need this `poetry.lock` file? Dependency management y'all!
Locking the packages to the exact version with which they were developed
with prevents all kind of problems, including weird version conflicts and
dependency management across other machines and developers.

### You do not activate the virtualenv!

----
**Note**

If you want the old way of doing things where one would just activate the virtualenv
to spawn a new shell, see the [poetry shell](https://python-poetry.org/docs/cli/#shell)
command.

----

Instead you use poetry's [run](https://python-poetry.org/docs/cli/#run) command. Remember the virtualenv that was created by
poetry in the last step?

`poetry run` will execute the given command in the project's virtualenv.

So for example, if you want to run the development server, instead of:

```shell
$ python manage.py runserver
```

you would now have to:

```shell
$ poetry run python manage.py runserver
```

----
**Note**

Even though there is a way to run `scripts` in poetry, it can only run python modules.
See https://github.com/python-poetry/poetry/issues/241 for methods on how to do implement
scripts/tasks like npm with custom wrappers.

----

### Extra: pip-tools!

## Easy development environments with Docker and docker-compose

----
**Note**

This will not be a tutorial about `Docker` or `docker-compose`. If you are not familiar
with either but want to use them,
[katacoda](https://katacoda.com/courses/container-runtimes) is a good resource to learn
from.

----

Development environments are hard to keep idempotent in nature. Given the vast amount of
distributions, operating systems, package managers available out there, it's hard to
provide a distributable development environment.

Virtual machines solved this problem, but they are way too heavy and clunky for just
development. Docker containers are lightweight "isolated" environments that are well
suited for development and one does not need to make changes to the host machine except
for the ability to run Docker and `docker-compose`.

There are lots of tutorials online for writing a `Dockerfile` for a Django project and a
corresponding `docker-compose` specification to use multiple services together.

```shell
$ docker-compose up -d
```

## Integrate static typing with `mypy` and `django-stubs`

## Easy linting with `flake8` and `wemake-python-stylguide`

## Opinionated code formatting using _Black_

## Automate typing/linting/formatting on commit using `pre-commit`

## py.test and GitHub CI integration

## Multiple Deployment Options with Herkou and Cloud Run.
