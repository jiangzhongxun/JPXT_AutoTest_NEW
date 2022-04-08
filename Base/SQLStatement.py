# 删除功能区表中IS_DELETE = 1的数据
areaFuncDelete = "DELETE FROM area_function WHERE IS_DELETE = 1;"
# 删除作业区中IS_DELETE = 1的数据
areaFuncInfoDelete = "DELETE FROM area WHERE IS_DELETE = 1;"
# 删除作业区中IS_DELETE = 1的暂存区矩阵
areaFuncMatrixDelete = "DELETE FROM area_row WHERE AREA_NO IN (SELECT AREA_NO FROM area WHERE IS_DELETE = 1);"
# 删除重复的集装箱类型
containerTypeDelete = "DELETE FROM container_type WHERE 1 ORDER BY ID DESC limit 1;"
# 两个查验
goodsCheck = "UPDATE entrust_info SET GOODS_TYPE = 'GOODS_CHECKED' WHERE GOODS_TYPE = 'WITHHOLD' AND TALLY_TYPE = 'TALLY_TYPE_SUCCEED' ORDER BY ID desc limit 2;"
# 两个放行
goodsRelease = "UPDATE entrust_info SET GOODS_TYPE = 'GOODS_RELEASED' WHERE GOODS_TYPE = 'WITHHOLD' AND TALLY_TYPE = 'TALLY_TYPE_SUCCEED' ORDER BY ID desc limit 2;"