package main.scala.com.liuhuang

class IntType(flag: String, default: String) extends ArgType {
  override def getFlag: String = flag
  override def getType: String = "Int"
  override def getDefault: String = default
  override def outTrueValue(value: String): Any = {
    if(value.isEmpty) return default.toInt
    value.toInt
  }
}
