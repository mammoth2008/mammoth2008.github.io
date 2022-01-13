#!/bin/sh

# 任一步骤执行失败都会终止整个部署过程
set -e

# 切换到 blog 文件夹
cd $HOME/Documents/1_writing/3_blog/mammoth2008.github.io

printf "\033[0;32mDeploying updates to GitHub...\033[0m\n"

# 构建静态内容
hugo # if using a theme, replace with `hugo -t <YOURTHEME>`

# 拷贝 slides 文件夹
cp -rf $HOME/Documents/2_hust/slides $HOME/Documents/1_writing/3_blog/mammoth2008.github.io/public

# 切换到 public 文件夹
cd public

# 添加更改到 git
git add -A

# 提交更改
msg="rebuilding site $(date)"
if [ -n "$*" ]; then
msg="$*"
fi
git commit -m "$msg"

# 推送到远程仓库
git push origin master

# 退回到上一级文件夹
cd ..

# print some message
printf "\n\n Uploading to blog repository...\n\n"

# Add, Commit, Push to Blog.
git add -A
msg="rebuilding site $(date)"
if [ -n "$*" ]; then
msg="$*"
fi
git commit -m "$msg"

# push到main分支
git push origin main

# 关闭proxy设置
# printf "\n\nClosing Proxy...\n\n"
# unset http_proxy; unset https_proxy; unset all_proxy
# printf "Proxy closed.\n\n"
# 
# # 部署到腾讯云
# tcb hosting deploy ./public  -e blog-3ganciy944986b42
# 
# # 打开proxy设置
# printf "\n\nreOpening Proxy...\n\n"
# export https_proxy=http://127.0.0.1:10080
# export http_proxy=http://127.0.0.1:10080
# export all_proxy=socks5://127.0.0.1:10081
# printf "Proxy opened again.\n\n"
# 
# # 删除腾讯云自动生成的log
# printf "Deleting CloudBase log.\n\n"
# rm -rf /Users/Freeman/cloudbase-framework
# printf "CloudBase Log deleted."
# 
printf "\n\n👻👻👻\nALL DONE\n😸😸😸\n\n"
