module Main where

main :: IO ()
main = do
    let bools = [True,False,True]
    let filterTrue = filter (==True)
    let filterTrueAndCount = (length . filterTrue)
    let result = filterTrueAndCount bools
    print result
    let result2 = (length. filter (==True)) bools
    print result2