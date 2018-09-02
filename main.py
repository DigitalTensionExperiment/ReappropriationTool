import mapping
import skeletoncomments

term = "mode"
key = "driver"
#object = mapping.Mapping()

#object.categories(term)
#object.key_in_values(key)

templateHCL = skeletoncomments.SkeletonComments()

file = '/template.hcl'

templateHCL.exraction(file)


