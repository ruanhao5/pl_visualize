# pl_visualize

## KITTI data

KITTI data had downloaded in `data` directory. I just put some sample of training dataset. KITTI data is `bin` format.

## mayavi

### install

> reference: [Win10（python3.6） 安装 mayavi4.6 - 简书 (jianshu.com)](https://www.jianshu.com/p/557371805562)

访问 https://www.lfd.uci.edu/~gohlke/pythonlibs/，下载以下四个whl（python3.6版本，win64位）文件：

> - mayavi-4.6.2+vtk81-cp36-cp36m-win_amd64（注意：是带vtk版本的mayavi，而且和下面的VTK版本对应）
> - PyQt4-4.11.4-cp36-cp36m-win_amd64
> - traits-4.6.0-cp36-cp36m-win_amd64
> - VTK-8.1.2-cp36-cp36m-win_amd64
>

其实上面的版本已经找不到了，但是只要是python3.6版本的就行。

我目前使用的是miniconda下的python3.6环境，对应的包放在`lib`文件夹下。

终端 cd 到 whl 存放目录，执行如下命令开始安装（**安装顺序为 PyQt、traits、VTK、mayavi**）

```bash
pip install xxx.whl
```

### get started

> reference: [【mayavi】显示 kitti 点云数据 - 灰信网（软件开发博客聚合） (freesion.com)](https://www.freesion.com/article/36131059149/)

```bash
python vision1.py
```

visualization of `data/000000.bin` of KIITI training dataset:

![](photo/vision1.bmp)


```bash
python vision2.py
```

visualization of `data/000001.bin` of KIITI training dataset:

![](photo/vision2.bmp)