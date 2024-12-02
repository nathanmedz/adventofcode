
import Data.List

first [] = []
first (x:xs) = x:second xs

second [] = []
second (x:xs) = first xs

readInt :: String -> Int
readInt = read

partone (left, right) = do
  putStrLn $ "Part 1: " ++ show (sum (map abs (zipWith (-) (sort left) (sort right))))

parttwo (left, right) = do
  putStrLn $ "Part 2: " ++ show  (sum (map (\x -> x * length (filter (==x) right)) left))


main = do 
  contents <- readFile "input.txt"
  let intList = map readInt $ words contents
  let (left, right) = (first intList, second intList) 
  partone(left, right)
  parttwo(left, right)
