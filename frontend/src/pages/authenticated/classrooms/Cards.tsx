import { useGetClassroomsQuery } from "@/services/cards";
import { useSelector } from "react-redux";
import Navbar from "./components/Navbar";
import StudyGroups from "./components/StudyGroups";
import { CreateClassRoomDialog } from "./components/CreateClassRoomDialog";
import { useEffect, useState } from "react";
import { Skeleton } from "@/components/ui/skeleton";

const Cards = () => {
  const user = useSelector((state: any) => state.auth.user);
  const { data, error, isLoading, refetch } = useGetClassroomsQuery(user.id, {
    refetchOnMountOrArgChange: true,
  });
  useEffect(() => {
    if (data?.length! > 0) {
      localStorage.setItem("Class length: ", data!.length.toString());
    }
  }, [data?.length]);

  const storedValue = localStorage.getItem("Class length: ");
  const setLength = storedValue !== null ? parseInt(storedValue, 10) : 0;

  
  return (
    <div className="text-center">
      <Navbar />
      <div className="max-w-[65%] mx-auto">
        <div className="flex justify-between">
          <h1 className="text-2xl">My Classrooms</h1>
          <CreateClassRoomDialog />
        </div>
        <div className="flex flex-row justify-center">
          {isLoading
            ? Array.from({ length: setLength }).map((_, index) => (
                <Skeleton
                  key={index}
                  className="w-[220px] h-[180px] rounded-md m-4"
                />
              ))
            : data?.map((studyGroup, i) => {
                return (
                  <StudyGroups
                    id={studyGroup.id}
                    key={i}
                    title={studyGroup.name}
                    description={studyGroup.description}
                  />
                );
              })}
        </div>
      </div>
    </div>
  );
};

export default Cards;
