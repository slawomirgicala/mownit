#include <stdio.h>
#include <gsl/gsl_blas.h>
#include <time.h>
#include <unistd.h>
#include <sys/times.h>
#include <limits.h>
#include <stdlib.h>
#include <sys/time.h>

#define LEV1OFF 10000000
#define LEV2OFF 1000


double lev1Multi(double *vec1, double *vec2, int length);
double lev2Multi(double *mat, int lin, int col, double *vec, int length);
void memFault(void);

int main(void){

	srand(time(NULL));
	
	FILE *fp;
	fp = fopen("blasTimesTest.csv", "w");
	if(fp == NULL){
		fprintf(stderr, "Unable to open file\n");
		exit(EXIT_FAILURE);
	}
	fprintf(fp, "\"level\";\"test_number\";\"vector_size\";\"time\"\n");
	

	for(unsigned long i = LEV1OFF; i <= LEV1OFF * 10; i += LEV1OFF / 2){

		double *a = calloc(i, sizeof(double));
                if(a == NULL) memFault();

                double *b = calloc(i, sizeof(double));
                if(b == NULL) memFault();

		for(unsigned long j = 0; j < i; j++){
			a[j] = (double) (rand() % 1000);
			b[j] = (double) (rand() % 1000);
		}
		for(int j = 1; j <= 10; j++){
			fprintf(fp, "1;%d;%lu;%.6lf\n", j, i, lev1Multi(a, b, i));
		}

		free(a);
		free(b);
	}

	printf("First level done.\n");

	
	for(unsigned long i = LEV2OFF; i <= LEV2OFF * 10; i += LEV2OFF / 2){

        	double *a = calloc(i * i, sizeof(double));
                if(a == NULL) memFault();

                double *b = calloc(i, sizeof(double));
                if(b == NULL) memFault();

		for(int j = 0; j < i*i; j++) a[j] = (double) (rand() % 1000);
		for(int j = 0; j < i; j++) b[j] = (double) (rand() % 1000);

                for(int j = 1; j <= 10; j++){
                	fprintf(fp, "2;%d;%lu;%.6lf\n", j, i, lev2Multi(a, i, i, b, i));
		}

                free(a);
                free(b);
        }

	printf("Second level done.\n");

	
	fclose(fp);

	return 0;
}


double lev1Multi(double *vec1, double *vec2, int length){
	struct timeval start, end;

	double res;
	gsl_vector_view A = gsl_vector_view_array(vec1, length);
	gsl_vector_view B = gsl_vector_view_array(vec1, length);

	gettimeofday(&start, NULL); 
	gsl_blas_ddot(&A.vector, &B.vector, &res);
	gettimeofday(&end, NULL);
	double time_taken; 
  
    	time_taken = (end.tv_sec - start.tv_sec) * 1e6; 
    	time_taken = (time_taken + (end.tv_usec - start.tv_usec)) * 1e-6; 
	
	return time_taken;
}

double lev2Multi(double *mat, int row, int col, double *vec, int length){
	struct timeval start, end;

        double res[row];
	for(int i = 0; i < row; i++){
		res[i] = 0;
	}

        gsl_matrix_view M = gsl_matrix_view_array(mat, row, col);
        gsl_vector_view V = gsl_vector_view_array(vec, length);
        gsl_vector_view C = gsl_vector_view_array(res, row);

	gettimeofday(&start, NULL);
	gsl_blas_dgemv(CblasNoTrans, 1.0, &M.matrix, &V.vector, 0.0, &C.vector);
	gettimeofday(&end, NULL);

	double time_taken; 
  
    	time_taken = (end.tv_sec - start.tv_sec) * 1e6; 
    	time_taken = (time_taken + (end.tv_usec - start.tv_usec)) * 1e-6; 
	
	return time_taken;
}


void memFault(void){
	fprintf(stderr, "Memory allocation fault\n");
	exit(EXIT_FAILURE);
}
