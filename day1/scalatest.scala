val bools = List(true,true,false)
val filterTrue: List[Boolean] => List[Boolean] = _.filter(_ == true)
val lengthFun: List[Boolean] => Int = _.length
val filterTrueAndCount: List[Boolean] => Int = lengthFun compose filterTrue 
println(filterTrueAndCount(bools))