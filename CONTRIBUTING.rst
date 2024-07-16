Contributing to FlaskCord
=============================

First of all, really thanks for considering this project and making contributions to improve it.

Any kind of improvements, feature additions, bug fixes, issues report or whatever which helps the library grow are welcomed. Just make sure that your part helps the library and its users in any way.

Basic Questions
---------------

If you're having any issue with the library itself, please do check if similar issue already exists in the `FlaskCord Issues`_ section. If you can't find any issue which helps you, then feel free to create a new one; check `Reporting New Issues`_ or just ask about it in ``#FlaskCord`` channel of our `Discord community`_.

.. _FlaskCord Issues: https://github.com/hunter87ff/FlaskCord/issues
.. _Discord community: https://discord.gg/7CrQEyP


Reporting New Issues
--------------------

Feel free to drop a new issue whenever you feel anything could be potentially be wrong with the library or if you're just stuck somewhere.

Make sure to include following information with your post.

- The expected workflow you were trying to achieve.
- If possible, include few steps to reproduce the situation.
- What actually happened or the full traceback.

Submitting Patches
------------------

You may optionally join our `Discord community`_ if you want to discuss in depth about the implementations before actually making the pull request. Ignore this if its obvious bug fix PR.

Minimal Style Guide
*******************

You may or may not find it much relevant but I prefer few conventions and code style, some of which are list below.

- Make use of present tense for your commit messages. For example, use "Fix state mismatch error" rather than "Fixed state mismatch error".
- You may or may not include docstrings. Although it's required but can also be added later on after making the PR.
- Prefer prefixing the commit messages with emojis. Check the `Emoji Usage Reference`_ for info on which emoji to use.
- Explicitly mention and inherit ``object`` when writing classes. For example, prefer ``class Foo(object): ...`` over ``class Foo: ...``.
- Prefer relative imports over absolute imports.

Emoji Usage Reference
*********************

Commits message looks nice on Github when they're prefixed with emojis. Prefer using any of the following emojis in your commit messages related to the following context.

- 🎨 ``:art:`` when improving the format/structure of the code.
- 🐎 ``:racehorse:`` when improving performance.
- 📝 ``:memo:`` when writing docs.
- 🐛 ``:bug:`` when fixing a bug.
- 💛 ``:yellow_heart:`` when adding a new feature.
- 🔒 ``:lock:`` when dealing with security.
- 👕 ``:shirt:`` when removing linter warnings.
- ✔ ``:heavy_check_mark:`` For anything else.