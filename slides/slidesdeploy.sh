#!/bin/sh

# 任一步骤执行失败都会终止整个部署过程
set -e

printf "Deploying SLIDES to GitHub..."

# 复制除了.git/之外的文件和文件夹
cp -R -f -v $HOME/Documents/2_hust/slides $HOME/Documents/1_writing/3_blog/mammoth2008.github.io/public
cd $HOME/Documents/1_writing/3_blog/mammoth2008.github.io/public/slides
rm -rf .git
rm .DS_Store
rm .gitignore
cd ..

git add -A

msg="rebuild SLIDES $(date)"

if [ -n "$*" ]; then
	msg="$*"
fi

git commit -m "$msg"

git push origin master

cd $HOME/Documents/2_hust/slides

git add -A

msg="rebuilding SLIDES $(date)"

if [ -n "$*" ]; then
	msg="$*"
fi

git commit -m "$msg"

git push origin main

printf "\n\n    🖥️  🖥️  🖥️ \nDEPLOY SLIDES DONE\n    ⌨️  ⌨️  ⌨️  \n\n"
