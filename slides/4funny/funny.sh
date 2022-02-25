function rand(){
    min=$1
    max=$(($2 - $min + 1))
    num=$(($RANDOM+1000000000)) # 增加一个10位的数再求余
    echo $(($num%$max + $min))
}

# 将最后一个数字改成题目数量
rand_no=$(rand 1 214)

open "/Users/Freeman/Documents/college/slides/4funny/funny$rand_no.html"
