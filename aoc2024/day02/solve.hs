readInt :: String -> Int
readInt = read

isStrictlyIncreasing :: [Int] -> Bool
isStrictlyIncreasing xs = all (\(x, y) -> (x < y) && abs (x-y) <= 3) (zip xs (tail xs))

isStrictlyDecreasing :: [Int] -> Bool
isStrictlyDecreasing xs = all (\(x, y) -> (x > y)  && abs (x-y) <= 3) (zip xs (tail xs))

isSafe :: [Int]  -> Bool
isSafe (x:y:xs) | x < y = isStrictlyIncreasing $ x:y:xs
                | x > y  =  isStrictlyDecreasing $ x:y:xs
                | otherwise = False

removeAt :: Int -> [a] -> [a]
removeAt idx xs = take idx xs ++ drop (idx + 1) xs

generateLists :: [a] -> [[a]]
generateLists xs = [removeAt i xs | i <- [0..length xs - 1]]

anySafe :: [Int] -> Bool
anySafe xs = any isSafe (generateLists xs)

partOne input = putStrLn . ("Part 1: " ++) . show . length . filter id $ map isSafe input

partTwo input = putStrLn . ("Part 1: " ++) . show . length .filter id $ map anySafe input


main :: IO ()
main = do
  contents <- readFile "input.txt"
  let input = map (map readInt . words) (lines contents)
  partOne input
  partTwo input