import System.IO  
import Data.Text
main = do  
    handle <- openFile "input.txt" ReadMode  
    contents <- hGetContents handle  
    hClose handle
    let lines = splitOn "\n" contents
    putStrLn lines