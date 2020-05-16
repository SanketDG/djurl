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

----
**Note**

This is an opinionated workflow of how to integrate and use Poetry in your Django projects.

----
### From requirements.txt to pyproject.toml

This is a tricky one! I have searched for tools that would automate this
process, but sadly there is none that works concretely.

[Relevant
commit](https://github.com/SanketDG/djurl/commit/86d29f453a00c702b35f81b1f27207640d563fb6)
where I create a pyproject.toml and run `poetry install` (explained in the next
section)

### Install dependencies and create virtualenv

### You do not activate the virtualenv!

### Extra: pip-tools!

## Easy development environments with Docker and docker-compose

## Integrate static typing with `mypy` and `django-stubs`

## Easy linting with `flake8` and `wemake-python-stylguide`

## Opinionated code formatting using _Black_

## Automate typing/linting/formatting on commit using `pre-commit`

## py.test and GitHub CI integration

## Multiple Deployment Options with Herkou and Cloud Run.
