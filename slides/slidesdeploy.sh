#!/bin/sh

# 任一步骤执行失败都会终止整个部署过程
set -e

printf "\033[0;32mDeploying SLIDES to GitHub...\033[0m\n"

cd $HOME/Documents/1_writing/3_blog/mammoth2008.github.io

# 复制除了.git/之外的文件和文件夹
cp -Rpf `ls $HOME/Documents/2_hust/slides |grep -v .git|xargs` $HOME/Documents/1_writing/3_blog/mammoth2008.github.io/public/slides

cd public

git add -A

msg="rebuilding site $(date)"
if [ -n "$*" ]; then
msg="$*"
fi

git commit -m "$msg"

git push origin master

printf "\n\n👻👻👻\nDEPLOY SLIDES\nALL DONE\n😸😸😸\n\n"
