import fx
from fx import *




class resetCloneOverride(Action):
	"""replicates the behavio or the clone tool "reset button", but resets clone frame as well"""
	def __init__(self,):
		Action.__init__(self, "KMFX|Clone Reset transforms and frame")

	def available(self):
			assert fx.viewer.toolName == "Clone","Clone tool only"

	def execute(self):
		beginUndo("Clone Reset transforms and frame") 

		node = activeNode()
		# print(node.state["paint"]["Clone.frame:0"])


		if node.type == "PaintNode":
			fx.activeProject().save() ##small hack to force the state to update

			clonelist = ["0","1"] ##both clone presets

			for n in clonelist:
				if node.state['paint']['Clone.frameRelative:'+n] == True:
					fx.paint.setState('Clone.frame:'+n, 0)

				else:
					fx.paint.setState('Clone.frame:'+n, player.frame)

				fx.paint.setState('Clone.position:'+n, Point3D(0,0))
				fx.paint.setState('Clone.rotate:'+n, 0)
				fx.paint.setState('Clone.scale:'+n, Point3D(1,1))
			fx.activeProject().save()

		endUndo()

addAction(resetCloneOverride())