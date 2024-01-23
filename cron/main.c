// im getting an error from regcomp because of no memory
// probably have some memory leak somewhere
#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
#include <string.h>
#include <regex.h>

#define LINE_LIMIT 16384
// eventually pass this as an argv
#define CRON_FILENAME "text.txt"

void main_loop ();
FILE *open_file (char *filename);
char *read_line(FILE* fp);
char **tokenize (char *line);
void print_tokens(char **tokens);
void print_description(char **tokens);
int validate_cron_line(char **tokens);
int validate_minutes(char *interval);
int process_interval(char *interval, int offset);
int is_star(char *interval);
void cleanup(FILE *fp);

int main() {
	main_loop();
	return 0;
}

void main_loop () {
	//char *status;
	char *line;
	char **tokens;
	FILE *fp = open_file(CRON_FILENAME);

	while ((line = read_line(fp)) != NULL) {
		printf("%s", line);
		tokens = tokenize(line);
		validate_cron_line(tokens);
		print_description(tokens);
		free(line);
		free(tokens);
	}
	cleanup(fp);
}

FILE *open_file (char *filename) {
	FILE *fp = fopen(filename, "r");
	if (!fp) {
		fprintf(stderr, "Could not open the file \"%s\"\n", filename);
		exit(EXIT_FAILURE);
	}
	return fp;
}

char *read_line(FILE* fp) {
	int line_max = LINE_LIMIT;

	char *line = malloc(line_max + 1);
	if (line == NULL) {
		fprintf(stderr, "Allocation failed miserably.\n");
		return NULL;
	}

	while (fgets(line, line_max + 1, fp) != NULL) {
		// if the line contains emptyness then drop it;
		
		if (line[0] != '\n' && line[1] != '\0' && line[0] != '#') {
			return line;
		}
	}
	return NULL;
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
	tokens[token_count] = token;
	token_count++;

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

int (*validation_funcs[]) (char *) = {
	&validate_minutes
};
char *interval_names[] = { "minute(s)", "hour(s)", "day of the month", "month", "day of the week" };

int validate_cron_line(char **tokens) {
	// simple one is if there are less than 5 tokens then for sure it's not good
	validation_funcs[0](tokens[0]);
	// add a for loop
	return 0;
}

int validate_minutes(char *interval) {
	regex_t regex;
	int reti;
	char msgbuf[100];
	const char *pattern = "^[0-5]?[0-9]$";

	// Compile regular expression
	reti = regcomp(&regex, pattern, REG_EXTENDED);
	if (reti != 0) {
		printf("Error code: %d\n", reti);
		fprintf(stderr, "Could not compile the regular expression.\n");
		regfree(&regex);
		exit(1);
	}

	// Execute regular expression
	reti = regexec(&regex, interval, 0, NULL, 0);
	if (!reti) {
		return 0;
	}
	else if (reti == REG_NOMATCH) {
		return(1);
	}
	else {
		regerror(reti, &regex, msgbuf, sizeof(msgbuf));
		fprintf(stderr, "Regex match failed: %s,\n", msgbuf);
		regfree(&regex);
		exit(1);
	}
	return 0;
}

void print_description(char **tokens) {
	for (int i = 0; i < 5; i++) {
		process_interval(tokens[i], i);
		if (i != 4) {
			printf(", ");
		}
	}
	printf("\n");
	printf("\n");
}

int process_interval(char *interval, int offset) {
	if (is_star(interval) == 0) {
		printf("%s", interval_names[offset]);
	}
	else {
		printf("at %s %s", interval_names[offset], interval);
	}
	return 0;
}

int is_star(char *interval) {
	if (strcmp(interval, "*") == 0) {
		printf("Every ");
		return 0;
	}
	else {
		return 1;
	}
}

void cleanup(FILE *fp) {
	if (fclose(fp) == 0) {
		fprintf(stdout, "Cleanup: the opened cron file has been properly closed\n");
	}
}
