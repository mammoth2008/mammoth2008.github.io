#!/bin/sh

# 任一步骤执行失败都会终止整个部署过程
set -e

printf "Deploying SLIDES to GitHub..."

cd $HOME/Documents/1_writing/3_blog/mammoth2008.github.io/public

rm -rf slides

mkdir slides

cd $HOME/Documents/2_hust/slides

# 复制除了.git/之外的文件和文件夹
cp -Rpf `ls $HOME/Documents/2_hust/slides |grep -v .git|xargs` $HOME/Documents/1_writing/3_blog/mammoth2008.github.io/public/slides

cd $HOME/Documents/1_writing/3_blog/mammoth2008.github.io/public

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
