# Contributing to AutoGPT Master Edition

First off, thank you for considering contributing to AutoGPT Master Edition. It's people like you that make AutoGPT Master Edition such a great tool.

## Where do I go from here?

If you've noticed a bug or have a feature request, make sure to check our [Issues](https://github.com/yourusername/autogpt_master/issues) page to see if someone else in the community has already created a ticket. If not, go ahead and [make one](https://github.com/yourusername/autogpt_master/issues/new)!

## Fork & create a branch

If this is something you think you can fix, then [fork AutoGPT Master Edition](https://help.github.com/articles/fork-a-repo) and create a branch with a descriptive name.

A good branch name would be (where issue #325 is the ticket you're working on):

```shell
git checkout -b 325-add-japanese-localisation
```

## Implement your fix or feature

At this point, you're ready to make your changes! Feel free to ask for help; everyone is a beginner at first.

## Get the code

The first thing you'll need to do is get the code. The easiest way to do this is to fork the project on GitHub, and then clone your repository:

```shell
git clone git@github.com:yourusername/autogpt_master.git
```

## Make sure the tests pass

Now, you'll want to start the application to see if everything works as expected. You should be able to start the application using the following command:

```shell
python autogpt_master.py --continuous
```

## Make your change

Next, make your changes to the codebase. Make sure your changes are as small as possible (as [atomic](https://en.wikipedia.org/wiki/Atomic_commit) as possible), and that the application still works after your changes.

## Write a good commit message

A good commit message serves at least three important purposes:

- To speed up the reviewing process.
- To help us write a good release note.
- To help the future maintainers of AutoGPT Master Edition (it could be you!), say five years into the future, to find out why a particular change was made to the code or why a specific feature was added.

Structure your commit message like this:

```
Short (50 chars or less) summary of changes

More detailed explanatory text, if necessary.  Wrap it to about 72
characters or so.  In some contexts, the first line is treated as the
subject of an email and the rest of the text as the body.  The blank
line separating the summary from the body is critical (unless you omit
the body entirely); tools like rebase can get confused if you run the
two together.

Further paragraphs come after blank lines.

- Bullet points are okay, too

- Typically a hyphen or asterisk is used for the bullet, followed by a
  single space, with blank lines in between, but conventions vary here

- Use a hanging indent
```

## Submit a pull request

Push to your fork and [submit a pull request](https://github.com/yourusername/autogpt_master/compare). In the pull request, choose a title which sums up the changes that you have made, and in the body provide more details about what your changes do. Also mention the number of the issue where discussion has taken place, for example "Closes #325".

Then sit back and wait. There will probably be discussion about the pull request and, if any changes are needed, we would love to work with you to get your pull request merged into AutoGPT Master Edition.

## What's in it for you?

Contributing to an open source project is a rewarding way to learn, teach, and build experience. Not only that, but by contributing to AutoGPT Master Edition you also get the opportunity to improve the tools that you use in your own projects.

Thank you for your contributions!
