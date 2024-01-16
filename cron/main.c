#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// pass a text file which will be read line by line
// pass a line to the tokenizer function until there is no lines left.
// we will read a line, then print it and next to it give the cron "explanation"
// each line will be tokenized based on spaces
// can have a function like translate to natural language, that will accept either several
// parameters or an array of values. each value will be mins, hours, day of month, etc... 
// validation function
// remember to ignore comments
// add proper clean up and closing of files
#define LINE_LIMIT 16384

char **tokenize (char *line);
void print_tokens(char **tokens);
void print_description(char **tokens);
int process_minutes(char *minutes);
int is_star(char *interval);
void cleanup(FILE *fp, char *line, char **tokens);

int main() {
	int line_max = LINE_LIMIT;
	char *filename = "cron.txt";
	char **tokens;

	FILE *fp = fopen(filename, "r");
	if (!fp) {
		fprintf(stderr, "Could not open the file \"%s\"\n", filename);
		exit(EXIT_FAILURE);
	}

	char *line = malloc(line_max + 1);
	if (line == NULL) {
		fprintf(stderr, "Allocation failed miserably.\n");
		return 1;
	}

	while (fgets(line, line_max + 1, fp) != NULL) {
		// if the line contains emptyness then drop it;
		if (line[0] != '\n' && line[1] != '\0') {
			// Process line, send it to a tokenizer
			tokens = tokenize(line);
			print_description(tokens);
			print_tokens(tokens);
		}
	}

	cleanup(fp, line, tokens);
	return 0;
}

#define TOKEN_ARRAY_SIZE 5
#define SEPARATOR " \n"
char **tokenize (char *line) {
	char *token;
	int token_array_size = TOKEN_ARRAY_SIZE;
	char **tokens = malloc(token_array_size * sizeof(char *));
	int token_count = 0;
	// later add realloc call to tokens and expand the project to actually possibly run programs

	if (!tokens) {
		fprintf(stderr, "Allocation failed miserably.\n");
		exit(EXIT_FAILURE);
	}
	token = strtok(line, SEPARATOR);

	while ((token = strtok(NULL, SEPARATOR))) {
		tokens[token_count] = token;
		token_count++;
	}

	return tokens;
}

void print_tokens(char **tokens) {
	for (int i = 0; i < TOKEN_ARRAY_SIZE; i++) {
		printf("%s\n", tokens[i]);
	}
}

int validate_cron_line(char **tokens) {
	// simple one is if there are less than 5 tokens then for sure it's not good
	return 0;
}

void print_description(char **tokens) {
	// tokens[0] - minute       # ┌───────────── minute (0–59)
	// tokens[1] - hour         # │ ┌───────────── hour (0–23)
	// tokens[2] - dayofmonth   # │ │ ┌───────────── day of the month (1–31)
	// tokens[3] - month        # │ │ │ ┌───────────── month (1–12)
	// tokens[3] - dayofweek    # │ │ │ │ ┌───────────── day of the week (0–6) (Sunday to Saturday;
	//                          # │ │ │ │ │                                   7 is Sunday on some systems)
	//                          # │ │ │ │ │
	//                          # │ │ │ │ │
	//                          # * * * * * <command>
	print_minutes(tokens[0]);
}

int process_minutes(char *minutes) {
	if (is_star(minutes) == 0) {
		printf("minute ");
		return 0;
	}
	int 
	next_field = strtok(minutes, "-");

}

int is_star(char *interval) {
	if (strlen(interval) == 1 && interval[0] == '*') {
		printf("Every ");
		return 0;
	}
	else {
		return 1;
	}
}

void cleanup(FILE *fp, char *line, char **tokens) {
	if (fclose(fp) == 0) {
		fprintf(stdout, "Cleanup: the opened cron file has been properly closed\n");
	}
	free(line);
	free(tokens);
}
