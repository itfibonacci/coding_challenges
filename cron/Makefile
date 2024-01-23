# Define the C compiler to use
CC = clang

# Define any compile-time flags
CFLAGS = -Wall -g

# Define the dir for object files and executables
OBJDIR = bin

# Define the C source files
SRCS = main.c

# Define the C object files 
OBJS = $(addprefix $(OBJDIR)/, $(SRCS:.c=.o))

# Define the executable file 
MAIN = $(OBJDIR)/cron

all: $(MAIN)

$(MAIN): $(OBJS)
	mkdir -p $(OBJDIR)
	$(CC) $(CFLAGS) -o $(MAIN) $(SRCS)

$(OBJDIR)/%.o: %.c
	mkdir -p $(OBJDIR)
	$(CC) $(CFLAGS) -c $<  -o $@

clean:
	$(RM) -r $(OBJDIR)
