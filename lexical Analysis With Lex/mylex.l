%{
#include<stdio.h>
#include<string.h>
int i = 0;
int n = 0;
int p = 0;
int o = 0;
int dtype = 0;
int k = 0;
int e = 0;
int tot = 0;
%}

%%
[a-z]+[(]+[)]																{printf("%s is a function\n",yytext); }
"int" || "Int" || "float"|| "Float" || "char" || "Char"  					{dtype++; printf("%s is a Data Type\n",yytext)}
"if" || "If" || "return" || "else" || "While" || "printf" || "scanf" 		{k++; printf("%s is a Keyword\n",yytext);}
([a-zA-Z0-9])*    															{i++; printf("%s is a Identifier\n",yytext);}
[-/+?0-9]*.[0-9]+ 															{n++; printf("%s is a Number\n",yytext);}
[(){}|,;:]  																	{p++; printf("%s is a Punctuator\n",yytext);}
[-+=]																		{o++; printf("%s is an Operator\n",yytext);}
[ ]																			{;}
["]+[%?a-zA-Z0-9 ]*+["]														{printf("%s is an String\n",yytext);}
#[a-zA-Z0-9 <>.]+															{printf("%s is a preprocessor\n",yytext); }
[\n]																		{printf("\n\n");}
. 																			{e++; printf("%s is unidentified \n",yytext);}
%%
  
int yywrap(void){ return 1; }
  
int main()
{   
	freopen("input.c","r",stdin);
    yylex();
	tot = dtype + k + i + n + p ;
	printf("The Total Number of Tokens are : %d \n",tot);
	printf("The Total Number of Unidentified lexems are : %d \n",e);
    return 0;
}