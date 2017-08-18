Module PiEstimate

    Sub Main()

        ' Read the number of samples to use from the user
        Console.Write("Number of Samples: ")
        Dim numSamples As Integer
        numSamples = Console.ReadLine()

        ' Allocate space for our random x & y coords, as well as a count of the
        ' number of points that fall within the radius of a quarter circle with
        ' radius 1
        Dim x As Single
        Dim y As Single
        Dim numWithinRadius As Integer = 0

        ' For each of the specified number of samples
        For n = 1 To numSamples

            ' generate an x and y coordiate between 0 and 1 -- [0,1) technically
            x = Rnd()
            y = Rnd()

            ' check if the point defined by the pair is less than a (euclidian) 
            ' distance of 1 unit from the origin. I.e. does the point fall within
            ' a quarter circle of radius one in the upper right quadrant?
            If Math.Sqrt(x * x + y * y) < 1 Then
                ' if it does, increment our count by one
                numWithinRadius = numWithinRadius + 1
            End If
        Next

        ' get the ratio of the number of samples within the quarter circle
        ' and to the total number of samples. This gives an estimate of the
        ' of one quarter of a circle with radius one
        Dim ratio As Double = numWithinRadius / numSamples

        ' multiply by a magic number, and we have an estimate for pi!
        Dim piEstimate = 4 * ratio

        Console.WriteLine("Number within radius: {0}", numWithinRadius)
        Console.WriteLine("Estimate for pi: {0}", piEstimate)

        ' keep console window open after output is given
        Console.ReadLine()


    End Sub

    Function randBetween(upperbound, lowerbound) As Integer
        Return CInt(Math.Floor((upperbound - lowerbound + 1) * Rnd())) + lowerbound

    End Function

End Module
