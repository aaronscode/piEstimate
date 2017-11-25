srand()

print("Number of Samples: ")
numSamples = parse(UInt64, readline())
#numSamples = 1000000000

numWithinRadius = 0

x = rand(numSamples)
y = rand(numSamples)

radii = sqrt(x.^2 .+ y.^2)
	
numWithinRadius = 0

for i = 1:numSamples
	if radii[i] < 1
		numWithinRadius += 1
	end
end

piEstimate = 4 * numWithinRadius / numSamples

print("Number of samples within radius: $numWithinRadius\n")
print("Estimate for pi: $piEstimate\n")
