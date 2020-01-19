# EXECUTABLE为目标的可执行文件名, 可以根据具体的情况对其进行修改。
EXECUTABLE := two_sum_c

UTILS_DIR := ../../utils/C

# 修改隐含规则中宏
CC := gcc
CFLAGS := -Wall -O2 -I$(UTILS_DIR)
# LDFLAGS+= -static
#LDFLAGS+= -lftd2xx


# 列出工作目录下所有以“.c”结尾的文件，以空格分隔，将文件列表赋给变量SOURCE
SOURCE := $(wildcard *.c)
SOURCE += $(wildcard $(UTILS_DIR)/*.c)

# 调用patsubst函数，生成与源文件对应的“.o”文件列表
OBJS := $(patsubst %.c, %.o, $(SOURCE))

# 编译所有".o"文件生成可执行文件
all : $(EXECUTABLE)
$(EXECUTABLE) : $(OBJS)
	@$(CC) $(CFLAGS) $(LDFLAGS) $(OBJS) -o $(EXECUTABLE)

# 声明伪目标
.PHONY : clean

# 删除所有中间文件和目标文件
clean :
	@rm -f $(EXECUTABLE) $(OBJS) *.o
