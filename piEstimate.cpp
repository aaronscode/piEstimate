#include <iostream>
#include <random>
#include <cmath>

using namespace std;

int main() {
	int numSamples, numWithinRadius = 0;

	cout << "Number of samples: ";
	cin >> numSamples;

	for(int i = 0; i < numSamples; i++){
		double x = (double) rand() / RAND_MAX;
		double y = (double) rand() / RAND_MAX;

		if(sqrt(x * x + y * y) < 1.0)
			numWithinRadius++;
	}

	double ratio = (double) numWithinRadius / numSamples;
	double piEstimate = 4.0 * ratio;

	cout << "Number of samples within radius: " << numWithinRadius << endl;
	cout << "Estimate for pi: " << piEstimate << endl;
}
