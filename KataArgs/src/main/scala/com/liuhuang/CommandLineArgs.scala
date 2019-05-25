package main.scala.com.liuhuang

import scala.util.matching.Regex

case class CommandLineArgs(inputParm: String) {

  val pattern = new Regex("\\s*-[a-z]\\s+((?!-[a-z]).)*")
  val cmdArgs: Map[String, String] = paserArgsToMap()

  def paserArgsToMap(): Map[String, String] = {
    (pattern findAllIn inputParm).map(x => {
      val field = x.split(" ")
      val flag = field(CmdLineArgEnum.FLAG)
      val value = if(isFlagHasValue(field)) field(CmdLineArgEnum.VALUE)  else  ""
      (flag, value)
    }).toMap
  }

  def isFlagHasValue(data: Array[String]): Boolean = {
    data.length != 1
  }

  def extractFlagVaule(flag: String): String = {
    cmdArgs(flag)
  }
}
