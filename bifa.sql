CREATE TABLE `bifa` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '必发比赛主键id',
  `zhu_team` varchar(45) NOT NULL COMMENT '主队名称',
  `ke_team` varchar(45) NOT NULL COMMENT '客队名称',
  `zhu_scores` tinyint(1) unsigned NOT NULL COMMENT '主队进球数',
  `ke_scores` tinyint(1) unsigned NOT NULL COMMENT '客队进球数',
  `screenings` int(10) unsigned NOT NULL COMMENT '当日比赛场次',
  `bifa_win` double unsigned NOT NULL COMMENT '必发投注主胜比例',
  `bifa_balance` double unsigned NOT NULL COMMENT '必发投注平比例',
  `bifa_fail` double unsigned NOT NULL COMMENT '必发投注主负比例',
  `real_result` tinyint(1) unsigned NOT NULL COMMENT '实际比赛结果',
  `bifa_result` tinyint(1) unsigned NOT NULL COMMENT '必发预测结果',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1