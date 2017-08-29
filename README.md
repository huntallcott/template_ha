## Repository template

To use the repository template, either [fork](https://help.github.com/articles/fork-a-repo/) or [clone](https://help.github.com/articles/duplicating-a-repository/) into a new GitHub repository.

Specifically, to clone:
1. Go to your GitHub home page, e.g. https://github.com/huntallcott
2. Click on the "+" sign to Create New Repository, called ProjectName
3. Open Git Bash
4. Type git clone --bare https://github.com/huntallcott/template_ha.git
5. Type git push --mirror https://github.com/huntallcott/ProjectName
6. Remove the old repository, by typing `cd..`, then `rm -rf template_ha.git`

MIT License

Copyright (c) 2017 Hunt Allcott

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
