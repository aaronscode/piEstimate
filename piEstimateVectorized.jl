srand()

print("Number of Samples: ")
numSamples = parse(UInt64, readline())
#numSamples = 100000000

numWithinRadius = 0

x = rand(numSamples)
y = rand(numSamples)

radii = sqrt(x.^2 .+ y.^2)
	
numWithinRadius = reduce(+, 0, map(Int, radii .< 1.0))

piEstimate = 4 * numWithinRadius / numSamples

print("Number of samples within radius: $numWithinRadius\n")
print("Estimate for pi: $piEstimate\n")
