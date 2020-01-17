//
// Created by tonycalvez on 17/01/2020.
//

FILE *fp;
char *command;

/* command contains the command string (a character array) */

/* If you want to read output from command */
fp = popen(command,"r");
/* read output from command */
fscanf(fp,....);   /* or other STDIO input functions */

fclose(fp);

/* If you want to send input to command */
fp = popen(command,"w");
/* write to command */
fprintf(fp,....);   /* or other STDIO output functions */

fclose(fp);