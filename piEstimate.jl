srand()

print("Number of Samples: ")
numSamples = parse(UInt64, readline())

numWithinRadius = 0

for i = 1:numSamples
	x = rand()
	y = rand()
	
	if sqrt(x^2 + y^2) < 1
		numWithinRadius += 1
	end
end

piEstimate = 4 * numWithinRadius / numSamples

print("Number of samples within radius: $numWithinRadius\n")
print("Estimate for pi: $piEstimate\n")
