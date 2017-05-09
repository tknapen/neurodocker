"""Utility functions for `neurodocker.interfaces.tests`."""
from __future__ import absolute_import

from neurodocker import Dockerfile, SpecsParser
from neurodocker.docker import client, DockerContainer, DockerImage

def get_container_from_specs(specs, **kwargs):
    """Return started container. `kwargs` are for `container.start()`."""
    parser = SpecsParser(specs)
    df = Dockerfile(parser.specs)
    image = DockerImage(df).build(log_console=True)
    return DockerContainer(image).start(**kwargs)

def test_cleanup(container):
    container.cleanup()
    client.containers.prune()
    client.images.prune()
