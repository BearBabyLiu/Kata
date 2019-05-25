package main.scala.com.liuhuang

trait ArgType {
  def getFlag: String
  def getDefault: String
  def getType:String
  def outTrueValue(value: String): Any
}
