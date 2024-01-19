#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <regex.h>
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

void main_loop ();
FILE *open_file (char *filename);
char *read_line(FILE* fp);
char **tokenize (char *line);
void print_tokens(char **tokens);
void print_description(char **tokens);
int validate_minutes(char *interval);
int process_minutes(char *minutes);
int process_interval(char *interval, int offset);
int is_star(char *interval);
void cleanup(FILE *fp);

int main() {
	main_loop();
	return 0;
}

void main_loop () {
	char *status;
	char *line;
	char **tokens;
	FILE *fp = open_file("cron.txt");

	while ((line = read_line(fp)) != NULL) {
		printf("%s", line);
		tokens = tokenize(line);
		//print_tokens(tokens);
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
	char **tokens;

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

int validate_cron_line(char **tokens) {
	// simple one is if there are less than 5 tokens then for sure it's not good
	return 0;
}

int (*validate_intervals[5])(char*) = { validate_minutes };

void print_description(char **tokens) {
	validate_intervals[0](tokens[0]);
	for (int i = 0; i < 5; i++) {
		process_interval(tokens[i], i);
		if (i != 4) {
			printf(", ");
		}
	}
	printf("\n");
	printf("\n");
}

char *interval_names[] = {"minute(s)", "hour(s)", "day of the month", "month", "day of the week"};

int validate_minutes(char *interval) {
	regex_t regex;
	int reti;
	char msgbuf[100];

	// Compile regular expression
	reti = regcomp(&regex, "^(\\*|[0-5]?0-9?(,[0-5]?0-9?)*)$", REG_EXTENDED);
	if (reti) {
		fprintf(stderr, "Could not compile the regular expression.\n");
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
		exit(1);
	}
	// Free memory allocated to the pattern buffer by regcomp()
	regfree(&regex);
	return 0;
}

int process_interval(char *interval, int offset) {
	if (is_star(interval) == 0) {
		printf("%s", interval_names[offset]);
	}
	else {
		printf("at %s %s", interval_names[offset], interval);
	}
	//validate_minutes(minutes);
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
