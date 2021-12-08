import java.io.File
import java.io.InputStream


fun preprocess(data: MutableList<String>): MutableList<MutableList<Int>> {
    val returnList: MutableList<MutableList<Int>> = mutableListOf<MutableList<Int>>()
    for (i in data.indices) {
        returnList.add(mutableListOf<Int>())
        data[i].forEach { returnList[i].add(it.digitToInt()) }
    }
    return returnList
}

fun countNumber(data: MutableList<MutableList<Int>>, index: Int, value: Int = 1): Int {
    var count:Int = 0
    for (subdata in data) {
        if (subdata[index] == value) count += 1
    }
    return count
}

fun filterArrays(data: MutableList<MutableList<Int>>, index: Int, value: Int): MutableList<MutableList<Int>> {
    val returnList: MutableList<MutableList<Int>> = mutableListOf<MutableList<Int>>()
    for (subdata in data) {
        if (subdata[index] == value) returnList.add(subdata)
    }
    return returnList
}

fun binToInt(data: MutableList<Int>): Int {
    var int: Int = 0
    for (i in data.indices) {
        int = int + data[data.lastIndex - i]*Math.pow(2.toDouble(), i.toDouble()).toInt()
    }
    return int
}

fun generateRating(data: MutableList<MutableList<Int>>, type_oxygen: Boolean = true): MutableList<Int> {
    var intermediate = data
    for (i in data[0].indices) {
        val count: Int = countNumber(intermediate, i)
        if (count > (intermediate.size - count)) { // 1 is most
            intermediate = filterArrays(intermediate, index = i, value = if (type_oxygen) 1 else 0)
        } else if (count < (intermediate.size - count)) { // 0 is most
            intermediate = filterArrays(intermediate, index = i, value = if (type_oxygen) 0 else 1)
        } else if (count == (intermediate.size - count)) {
            intermediate = filterArrays(intermediate, index = i, value = if (type_oxygen) 1 else 0)
        }
        if (intermediate.size == 1) {
            break
        }
    }
    return intermediate[0]
}

fun process(data: MutableList<MutableList<Int>>) {
    val o2Rating = binToInt(generateRating(data))
    val co2Rating = binToInt(generateRating(data, false))
    println("O2 Rating: ${o2Rating}\nCO2 Rating: ${co2Rating}\nResult: ${o2Rating*co2Rating}")
}

fun main() {
    val _input: InputStream = File("./Input1.txt").inputStream()  // Input is the same
    val input: MutableList<String> = mutableListOf<String>()
    _input.bufferedReader().forEachLine { input.add(it) }
    val data: MutableList<MutableList<Int>> = preprocess(input)
    process(data)
}

main()