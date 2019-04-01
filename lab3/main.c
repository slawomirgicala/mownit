#include <stdio.h>
#include <gsl/gsl_blas.h>
#include <time.h>
#include <unistd.h>
#include <sys/times.h>
#include <limits.h>
#include <stdlib.h>
#include <sys/time.h>



double better_multi(double** A, double** B, int m, int n, int p);
double naive_multi(double** A, double** B, int m, int n, int p);
double blas_multi(double** A, double** B, int m, int n, int p);

void memFault(void);

int main(void){

    srand(time(NULL));

    FILE *fp;
    fp = fopen("matrix_Multi_in_C_with_opti.csv", "w");
    if(fp == NULL){
        fprintf(stderr, "Unable to open file\n");
        exit(EXIT_FAILURE);
    }
    fprintf(fp, "\"type\";\"test_number\";\"matrix_size\";\"time\"\n");

    int test_sizes[] = {10,20,50,100,250,500,750,1000};

    for (int i = 0; i < 8; ++i) {
        int s = test_sizes[i];

        double** a = malloc(s * sizeof(double*));
        if(a == NULL) memFault();

        double** b = malloc(s * sizeof(double*));
        if(b == NULL) memFault();

        for (int k = 0; k < s; ++k) {
            a[k] = malloc(s * sizeof(double));
            b[k] = malloc(s * sizeof(double));
        }



        for (int row = 0; row < s; ++row) {
            for (int col = 0; col < s; ++col) {
                a[row][col] = 0.69*(double)(rand()%100);
                b[row][col] = 0.69*(double)(rand()%100);
            }
        }

        for (int j = 0; j < 10; ++j) {
            fprintf(fp, "%s;%d;%d;%.6lf\n", "naive", j, test_sizes[i], naive_multi(a,b,s,s,s));
            fprintf(fp, "%s;%d;%d;%.6lf\n", "better", j, test_sizes[i], better_multi(a,b,s,s,s));
            fprintf(fp, "%s;%d;%d;%.6lf\n", "blas", j, test_sizes[i], blas_multi(a,b,s,s,s));
        }


        for (int k = 0; k < s; ++k) {
            free(a[k]);
            free(b[k]);
        }
        free(a);
        free(b);

    }


    fclose(fp);

    return 0;
}


double better_multi(double** A, double** B, int m, int n, int p){
    struct timeval start, end;


    double** C = malloc(m * sizeof(double*));

    for (int k = 0; k < m; ++k) {
        C[k] = malloc(p * sizeof(double));
    }



    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < p; ++j) {
            C[i][j] = 0;
        }
    }

    gettimeofday(&start, NULL);

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < p; ++j) {
            for (int k = 0; k < n; ++k) {
                C[i][j] = C[i][j] + A[i][k] * B[k][j];
            }
        }
    }



    gettimeofday(&end, NULL);
    double time_taken;

    time_taken = (end.tv_sec - start.tv_sec) * 1e6;
    time_taken = (time_taken + (end.tv_usec - start.tv_usec)) * 1e-6;

    for (int l = 0; l < m; ++l) {
        free(C[l]);
    }

    free(C);

    return time_taken;
}

double naive_multi(double** A, double** B, int m, int n, int p){
    struct timeval start, end;


    double** C = malloc(m * sizeof(double*));

    for (int k = 0; k < m; ++k) {
        C[k] = malloc(p * sizeof(double));
    }


    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < p; ++j) {
            C[i][j] = 0;
        }
    }

    gettimeofday(&start, NULL);

    for (int j = 0; j < p; ++j) {
        for (int k = 0; k < n; ++k) {
            for (int i = 0; i < m; ++i) {
                C[i][j] = C[i][j] + A[i][k] * B[k][j];
            }
        }
    }



    gettimeofday(&end, NULL);
    double time_taken;

    time_taken = (end.tv_sec - start.tv_sec) * 1e6;
    time_taken = (time_taken + (end.tv_usec - start.tv_usec)) * 1e-6;

    for (int l = 0; l < m; ++l) {
        free(C[l]);
    }

    free(C);

    return time_taken;
}

double blas_multi(double** A, double** B, int m, int n, int p){
    struct timeval start, end;

    double* c = malloc(m * p * sizeof(double));
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < p; ++j) {
            c[i*p + j] = 0;
        }
    }

    double* a = malloc(m * n * sizeof(double));
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            a[i*n + j] = A[i][j];
        }
    }

    double* b = malloc(n * p * sizeof(double));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < p; ++j) {
            b[i*p + j] = B[i][j];
        }
    }



    gsl_matrix_view m1 = gsl_matrix_view_array(a,(const size_t) m, (const size_t)n);
    gsl_matrix_view m2 = gsl_matrix_view_array(b, (const size_t)n, (const size_t)p);
    gsl_matrix_view res = gsl_matrix_view_array(c, (const size_t)m, (const size_t)p);


    gettimeofday(&start, NULL);

    gsl_blas_dgemm(CblasNoTrans, CblasNoTrans, 1.0, &m1.matrix, &m2.matrix, 0.0, &res.matrix);

    gettimeofday(&end, NULL);



    free(a);
    free(b);
    free(c);


    double time_taken;

    time_taken = (end.tv_sec - start.tv_sec) * 1e6;
    time_taken = (time_taken + (end.tv_usec - start.tv_usec)) * 1e-6;

    return time_taken;
}


void memFault(void){
    fprintf(stderr, "Memory allocation fault\n");
    exit(EXIT_FAILURE);
}