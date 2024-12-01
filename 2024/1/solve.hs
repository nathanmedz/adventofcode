import Data.List

strToInt :: String -> Int
strToInt = read

first [] = []
first (x:xs) = x:second xs

second [] = []
second (x:xs) = first xs

partone = do
  contents <- readFile "input.txt"
  let intList = map strToInt $ words contents
  let left = sort $ first intList
  let right = sort $ second intList  
  let zipped = zipWith (-) left right
  let distances = map abs zipped
  print $ sum distances


main = 
  do partone