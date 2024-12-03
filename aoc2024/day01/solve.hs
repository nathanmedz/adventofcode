import Data.List (sort)

splitEvenOdd :: [a] -> ([a], [a])
splitEvenOdd xs = (evenIndexed, oddIndexed)
  where
    evenIndexed = [x | (x, i) <- zip xs [0..], even i]
    oddIndexed  = [x | (x, i) <- zip xs [0..], odd i]


partOne :: [Int] -> [Int] -> IO ()
partOne left right = do
  putStrLn . ("Part 1: " ++) . show . sum . map abs . zipWith (-) (sort left) . sort $ right


partTwo :: [Int] -> [Int] -> IO ()
partTwo left right = do
  putStrLn . ("Part 2: " ++) . show . sum . map (\x -> x * length (filter (==x) right)) $ left


main :: IO ()
main = do
  contents <- readFile "input.txt"
  let intList = map read . words $ contents
  let (left, right) = splitEvenOdd intList
  partOne left right
  partTwo left right
