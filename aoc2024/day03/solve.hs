
import Text.Regex.TDFA

readInt :: String -> Int
readInt = read

main :: IO ()
main = do
  contents <- readFile "./test.txt"
  let regex = "mul\\(([0-9]{1,3}),([0-9]{1,3})\\)"

  let result = getAllTextMatches $ contents =~ regex :: [String]
  print result