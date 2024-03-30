#include <complex>
#include <fstream>

int calcMandel(int x, int y, int maxIts, double xDivFactor, double yDivFactor){
    std::complex<double> z = (0.0, 0.0);
    double newX = x / xDivFactor;
    double newY = y / yDivFactor;
    std::complex<double> c;
    //For some reason, doing c = (newX, newY) always gave (-1, 0) so used this instead
    c.real(newX);
    c.imag(newY);
    for (int k = 0; k < maxIts; k++){
        z = pow(z, 2) + c;
        if (abs(z) > 2){
            return k;
        }
    }
    return 0;
}

int main(){
    int width = 3840;
    int height = 2400;
    int xMid = width / 2 + width / 4;
    int yMid = height / 2;
    double xDivFactor = width / 3;
    double yDivFactor = height / 2;
    int maxIts = 25;
    std::ofstream f;
    f.open("mandelbrotVals.txt");
    f << width << "," << height << ",";
    for (int j = 0; j < height; j++){
        for (int i = 0; i < width; i++){
            int x = i - xMid;
            f << calcMandel(x, j - yMid, maxIts, xDivFactor, yDivFactor) << ",";;
        }
    }
    f.close();
}