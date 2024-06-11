package com.example.project3

import java.util.*
import kotlin.math.max

var N = 0
var M = 0
val dy = arrayOf(-1, 0, 1, 0)
val dx = arrayOf(0, 1, 0, -1)
lateinit var lab: Array<IntArray>
lateinit var tmpLab: Array<IntArray>
var virusList = ArrayList<Virus>()
var ans = 0

data class Virus(var x:Int, var y:Int)


fun main() {
    val sc = Scanner(System.`in`)
    N = sc.nextInt()
    M = sc.nextInt()
    sc.nextLine()

    lab = Array(N,{IntArray(M)})

    for (i in lab.indices) {
        for (j in lab[0].indices) {
            lab[i][j] = sc.nextInt()
            if (lab[i][j] == 2) {
                virusList.add(Virus(i, j))
            }
        }
    }
    tmpLab = Array(N) { IntArray(M) }

    for (i in lab.indices) {
        for (j in lab[0].indices) {
            if (lab[i][j] == 0) {
                for (i in 0 until N)
                    for (j in 0 until M)
                        tmpLab[i][j] = lab[i][j]

                tmpLab[i][j] = 1
                wall(1)
            }
        }
    }

    println(ans)
}


fun wall(count:Int) {
    if (count == 3) {
        var spreadLab = Array(N) { IntArray(M) }
        for (i in 0 until N)
            for (j in 0 until M)
                spreadLab[i][j] = tmpLab[i][j]
        spread(spreadLab)
        return
    }

    for (i in lab.indices) {
        for (j in lab[0].indices) {
            if (tmpLab[i][j] == 0) {
                tmpLab[i][j] = 1
                wall(count + 1)
                tmpLab[i][j] = 0
            }
        }
    }
}


fun spread(spreadLab: Array<IntArray>) {

    val queue: Queue<Virus> = LinkedList()
    for (virus in virusList) {
        queue.add(virus)
    }
    while (!queue.isEmpty()) {
        var virus = queue.poll()

        for (i in 0..3) {
            var nx = virus.x + dx[i]
            var ny = virus.y + dy[i]

            if (0 <= nx && nx < N && 0 <= ny && ny < M) {
                if (spreadLab[nx][ny] == 0) {
                    spreadLab[nx][ny] = 2;
                    queue.add(Virus(nx, ny))
                }
            }
        }
    }

    var count = 0
    for (i in 0 until N) {
        for (j in 0 until M) {
            if (spreadLab[i][j] == 0)
                count++
        }
    }
    ans = max(ans, count)
}