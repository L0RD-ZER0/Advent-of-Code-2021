import java.io.File
import java.io.InputStream

// Transpose the matrix of input
fun preprocess(data: MutableList<String>): MutableList<MutableList<Int>> {
    val returnList: MutableList<MutableList<Int>> = mutableListOf<MutableList<Int>>()
    for (bytes in data) {
        for (i in bytes.indices) {
            try {
                returnList[i].add(bytes[i].digitToInt())
            } catch ( err: IndexOutOfBoundsException ) {
                returnList.add(index = i, element = mutableListOf<Int>())
                returnList[i].add(bytes[i].digitToInt())
            }
        }
    }
    return returnList
}

fun getCountOf(data: MutableList<Int>, element: Int): Int {
    return data.count { it == element }
}

fun binToInt(data: MutableList<Int>): Int {
    var int: Int = 0
    for (i in data.indices) {
        int = int + data[data.lastIndex - i]*Math.pow(2.toDouble(), i.toDouble()).toInt()
    }
    return int
}

fun binInverter(data: MutableList<Int>): MutableList<Int> {
    val inverted: MutableList<Int> = mutableListOf<Int>()
    for (i in data) {
        inverted.add( if (i==0) 1 else 0 )
    }
    return inverted
}

fun process(data: MutableList<MutableList<Int>>) {
    val bits: MutableList<Int> = mutableListOf<Int>()
    for (subdata in data) {
        if (getCountOf(subdata, 1) > subdata.size/2) {
            bits.add(1)
        } else {
            bits.add(0)
        }
    }
    val gamma: Int = binToInt(bits)
    val epsilon: Int = binToInt(binInverter(bits))
    println("Gamma: ${gamma}\nEpsilon: ${epsilon}\nResult: ${gamma*epsilon}")
}

fun main() {
    val _input: InputStream = File("./Input1.txt").inputStream()
    val input: MutableList<String> = mutableListOf<String>()
    _input.bufferedReader().forEachLine { input.add(it) }
    val data: MutableList<MutableList<Int>> = preprocess(input)
    process(data)
}

main()