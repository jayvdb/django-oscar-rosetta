from oscar.core.application import OscarConfig


class OscarRosettaConfig(OscarConfig):

    name = "oscar_rosetta"
    label = "oscar_rosetta"
    verbose_name = 'Oscar Rosetta'
    namespace = "oscar_rosetta"

    default_permissions = ["is_staff"]
