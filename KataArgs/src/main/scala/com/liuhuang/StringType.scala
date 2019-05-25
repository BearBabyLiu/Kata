package main.scala.com.liuhuang

class StringType(flag: String, default: String) extends ArgType {
  override def getFlag: String = flag
  override def getType: String = "String"
  override def getDefault: String = default
  override def outTrueValue(value: String): Any = {
    value
  }
}
