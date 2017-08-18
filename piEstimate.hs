module Main where

import System.Random

main :: IO ()
main = do
  putStrLn "Number of samples: "
  numSamplesStr <- getLine
  let numSamples = read numSamplesStr :: Int

  g1 <- getStdGen
  g2 <- newStdGen
  
  let pairs = genPairs g1 g2 numSamples
  let estimate = piEstimate numSamples $ numInside pairs

  putStrLn ("Points inside: " ++ show (numInside pairs))
  putStrLn ("Estimate of pi: " ++ show estimate)

genPairs :: StdGen -> StdGen -> Int -> [(Float, Float)]
genPairs g1 g2 numSamples = zip (take numSamples (randoms g1 :: [Float]) ) (take numSamples (randoms g2 :: [Float]))
  
numInside :: [(Float, Float)] -> Int
numInside pairs = length $ filter isInsideCircle pairs

isInsideCircle :: (Float, Float) -> Bool
isInsideCircle (x, y)  
  | sqrt ((x * x) + (y * y)) < 1.0 = True
  | otherwise = False

piEstimate :: Int -> Int -> Float
piEstimate a b = fromIntegral b / fromIntegral a * 4.0
