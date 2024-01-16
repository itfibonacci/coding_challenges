# Define the C compiler to use
CC = clang

# Define any compile-time flags
CFLAGS = -Wall -g

# Define the C source files
SRCS = main.c

# Define the C object files 
OBJS = $(SRCS:.c=.o)

# Define the executable file 
MAIN = cron

all: $(MAIN)

$(MAIN): $(OBJS)
	$(CC) $(CFLAGS) -o $(MAIN) $(SRCS)

.c.o:
	$(CC) $(CFLAGS) -c $<  -o $@

clean:
	$(RM) $(MAIN)
